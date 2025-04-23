const readMoreButton = document.getElementById('readMoreButton');
const readMoreText = document.getElementById('readMoreText');
const readMoreGradient = document.getElementById('readMoreGradient');

readMoreButton.addEventListener('click', function () {
  const isExpanded = this.getAttribute('aria-expanded') === 'true';

  if (isExpanded) {
    readMoreText.style.maxHeight = '350px';
    this.setAttribute('aria-expanded', 'false');
    this.innerHTML = 'Читать все ↓';
    readMoreGradient.style.display = 'block';
  } else {
    readMoreText.style.maxHeight = readMoreText.scrollHeight + 'px';
    this.setAttribute('aria-expanded', 'true');
    this.innerHTML = 'Свернуть ↑';
    readMoreGradient.style.display = 'none';
  }
});