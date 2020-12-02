window.onload = () => {
  let submitBtn = document.getElementById("login");
  submitBtn.addEventListener("click", (e) => {
    e.preventDefault();
    let form = new FormData("#form_login");
    const csrfmiddlewaretoken = document.querySelector(
      "[name=csrfmiddlewaretoken]"
    ).value;
    const headers = { "X-CSRFToken": csrfmiddlewaretoken };

    fetch("", {
      method: "POST",
      headers: headers,
      body: form,
    });
  });
};

const username = document.getElementById("username").value;
const password = document.getElementById("password").value;

form.append("username", username);
form.append("password", password);
