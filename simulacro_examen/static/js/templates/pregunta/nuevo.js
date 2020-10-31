window.onload = async () => {
  //let editors = document.querySelectorAll("[dir=ltr]");
  ////let pregunta_editor = new Array(editors).shift()
  ////pregunta_editor.style.width = '60vw'
  //for (editor of editors) {
  //console.log("editors");
  //editor.style.width = "60vw";
  //}
  //editors.map(editor => {
  //})
  //
  await sleep(500)
  CKEDITOR.instances["id_contenido"].resize('60vw', 400)
  CKEDITOR.instances["id_alt_1-alternativa"].resize('60vw', 200)
  CKEDITOR.instances["id_alt_2-alternativa"].resize('60vw', 200)
  CKEDITOR.instances["id_alt_3-alternativa"].resize('60vw', 200)
  CKEDITOR.instances["id_alt_4-alternativa"].resize('60vw', 200)
  CKEDITOR.instances["id_alt_5-alternativa"].resize('60vw', 200)
};

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
