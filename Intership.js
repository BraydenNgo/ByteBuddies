function handlePronounChange() {
    var select = document.getElementById("pronouns-select");
    var customInput = document.getElementById("pronouns-custom");
    
    if (select.value === "custom") {
      customInput.style.display = "block";
    } else {
      customInput.style.display = "none";
    }
  }