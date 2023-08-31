const targetNumber = Math.floor(Math.random() * 100) + 1;
const guessInput = document.getElementById("guessInput");
const submitBtn = document.getElementById("submitBtn");
const guessOutcome = document.getElementById("guessOutcome");

submitBtn.addEventListener("click", () => {
  const userGuess = parseInt(guessInput.value);

  if (userGuess === targetNumber) {
    guessOutcome.textContent = "Correct guess!";
  } else if (userGuess < targetNumber) {
    guessOutcome.textContent = "Your guess is too low.";
  } else {
    guessOutcome.textContent = "Your guess is too high.";
  }
});
