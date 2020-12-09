window.onload = async () => {
  await sleep(400)
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
