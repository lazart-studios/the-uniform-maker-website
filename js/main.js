document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const panel = document.querySelector('.nav-panel');

  if (toggle && panel) {
    toggle.addEventListener('click', () => {
      const open = panel.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });

    document.querySelectorAll('.nav-group').forEach(group => {
      const button = group.querySelector('.nav-group-toggle');
      if (!button) return;
      button.addEventListener('click', () => {
        if (window.innerWidth > 1180) return;
        const open = group.classList.toggle('open');
        button.setAttribute('aria-expanded', String(open));
      });
    });

    panel.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        panel.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        document.querySelectorAll('.nav-group.open').forEach(group => {
          group.classList.remove('open');
          const button = group.querySelector('.nav-group-toggle');
          if (button) button.setAttribute('aria-expanded', 'false');
        });
      });
    });
  }

  const quoteForm = document.querySelector('#quote-form');
  if (quoteForm) {
    const model = quoteForm.querySelector('#quote-model');
    const material = quoteForm.querySelector('#quote-material');
    const branding = quoteForm.querySelector('#quote-branding');
    const quantity = quoteForm.querySelector('#quote-quantity');
    const deadline = quoteForm.querySelector('#quote-deadline');
    const addonInputs = Array.from(quoteForm.querySelectorAll('.addon-option input'));
    const total = quoteForm.querySelector('#estimate-total');
    const breakdown = quoteForm.querySelector('#estimate-breakdown');
    const summary = quoteForm.querySelector('#quote-summary-text');

    const euro = value => `€${Math.round(value).toLocaleString('en-US')}`;

    const calculate = () => {
      const quantityValue = Math.max(Number(quantity?.value || 0), 10);
      const modelPrice = Number(model?.selectedOptions[0]?.dataset.price || 0);
      const materialPrice = Number(material?.selectedOptions[0]?.dataset.price || 0);
      const brandingPrice = Number(branding?.selectedOptions[0]?.dataset.price || 0);
      const deadlineMultiplier = Number(deadline?.selectedOptions[0]?.dataset.multiplier || 1);
      const addons = addonInputs.filter(input => input.checked);
      const addonsPerPiece = addons.reduce((sum, input) => sum + Number(input.value || 0), 0);

      const subtotalPerPiece = modelPrice + materialPrice + brandingPrice + addonsPerPiece;
      const estimate = subtotalPerPiece * quantityValue * deadlineMultiplier;
      const addonsLabel = addons.length ? addons.map(input => input.dataset.label).join(', ') : 'fără extra opționale';
      const modelLabel = model?.selectedOptions[0]?.textContent || 'model standard';
      const materialLabel = material?.selectedOptions[0]?.textContent || 'material standard';
      const brandingLabel = branding?.selectedOptions[0]?.textContent || 'fără branding';

      if (total) total.textContent = euro(estimate);
      if (breakdown) breakdown.textContent = `${quantityValue} buc · ${modelLabel.toLowerCase()} · ${materialLabel.toLowerCase()}`;
      if (summary) summary.textContent = `${modelLabel}, ${quantityValue} bucăți, ${materialLabel.toLowerCase()}, ${brandingLabel.toLowerCase()}, ${addonsLabel}.`;
    };

    [model, material, branding, quantity, deadline, ...addonInputs].forEach(field => {
      field?.addEventListener('input', calculate);
      field?.addEventListener('change', calculate);
    });

    calculate();
  }

  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', event => {
      event.preventDefault();
      const button = form.querySelector('button[type="submit"]');
      if (button) {
        const original = button.textContent;
        button.textContent = 'Trimis';
        button.disabled = true;
        setTimeout(() => {
          button.textContent = original;
          button.disabled = false;
        }, 2000);
      }
    });
  });
});
