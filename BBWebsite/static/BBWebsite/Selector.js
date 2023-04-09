const cards = document.querySelectorAll('.card');

cards.forEach((card) => {
  const acceptButton = card.querySelector('.accept');
  acceptButton.addEventListener('click', () => {
    console.log(card)
    card.remove();
  });

  cards.forEach(card => {
    const declineButton = card.querySelector('.decline');
    declineButton.addEventListener('click', () => {
      card.remove();
    });
  });
});