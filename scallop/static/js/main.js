const animation = document.querySelector('#scallop-animation');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

// Keep native controls available if autoplay is blocked or JavaScript is disabled.
if (!reducedMotion.matches) {
  animation.play().catch(() => {});
}
reducedMotion.addEventListener('change', (event) => {
  if (event.matches) animation.pause();
});

const copyButton = document.querySelector('#copy-citation');
const citation = document.querySelector('#citation');
const copyStatus = document.querySelector('#copy-status');
copyButton.hidden = false;

copyButton.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(citation.textContent.trim());
    copyStatus.textContent = 'Citation copied to clipboard.';
  } catch {
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(citation);
    selection.removeAllRanges();
    selection.addRange(range);
    copyStatus.textContent = 'Citation selected. Press Ctrl+C or ⌘C to copy.';
  }
});
