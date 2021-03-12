window.onload = async () => {
  reload_condicional()
  await sleep(200)
  CKEDITOR.instances["id_contenido"].resize('40vw', 400)
  CKEDITOR.instances["id_alt_1-alternativa"].resize('40vw', 220)
  CKEDITOR.instances["id_alt_2-alternativa"].resize('40vw', 220)
  CKEDITOR.instances["id_alt_3-alternativa"].resize('40vw', 220)
  CKEDITOR.instances["id_alt_4-alternativa"].resize('40vw', 220)
  CKEDITOR.instances["id_alt_5-alternativa"].resize('40vw', 220)

};

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

const reload_condicional = () => {

  if (sessionStorage.getItem('reload') === null) {
    sessionStorage.setItem('reload', 1)
  } else if (sessionStorage.getItem('reload') === '0') {
    sessionStorage.setItem('reload', 1)
    window.location.href = window.location.href
  } else if (sessionStorage.getItem('reload') === '1') {
    sessionStorage.setItem('reload', 0)
  }

}
