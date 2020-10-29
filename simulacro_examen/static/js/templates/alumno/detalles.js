window.onload = () => {
  const update_alumno_btn = document.querySelector('#update_alumno')
  update_alumno_btn.addEventListener('click', e => {
    e.preventDefault()
    sendPutRequest()
  })
}

const sendPutRequest = () => {
  const url = document.location.href
  const csrfmiddlewaretoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  const headers = { "X-CSRFToken": csrfmiddlewaretoken };

  const formData = new FormData(document.querySelector('#form_alumno'))

  fetch(url, {
    method: 'POST',
    headers: headers,
    body: formData,
  })
}
