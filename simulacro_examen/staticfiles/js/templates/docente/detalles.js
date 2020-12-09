window.onload = () => {
  const update_docente_btn = document.querySelector("#update_docente");
  update_docente_btn.addEventListener("click", (e) => {
    e.preventDefault();
    sendPutRequest();
  });
};

const sendPutRequest = () => {
  const url = document.location.href;
  const csrfmiddlewaretoken = document.querySelector(
    "[name=csrfmiddlewaretoken]"
  ).value;
  const headers = { "X-CSRFToken": csrfmiddlewaretoken };

  const formData = new FormData(document.querySelector("#form_docente"));

  fetch(url, {
    method: "POST",
    headers: headers,
    body: formData,
  });
};
