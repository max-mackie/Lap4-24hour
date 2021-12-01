pieceCount = document.getElementById("piece_count");
predictSubmit = document.getElementById("predict-submit");
predictResult = document.getElementById("result");

toEmail = document.getElementById("to-email");
mailSubmit = document.getElementById("mail-submit");

pieceCount.addEventListener("change", () => {
  validateSubmission();
});

toEmail.addEventListener("input", (e) => {
  const emailInputValue = e.currentTarget.value;
  if (
    /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/.test(emailInputValue) !=
    true
  ) {
    mailSubmit.disabled = true;
  } else {
    mailSubmit.disabled = false;
  }
});

function validateSubmission(e) {
  predictSubmit.disabled = validatePieceCount();
}

function validatePieceCount() {
  return parseInt(pieceCount.value) < 20;
}

function validateEmail(e) {
  mailSubmit.disabled = !e.target.value || !parseInt(predictResult.innerText);
}
