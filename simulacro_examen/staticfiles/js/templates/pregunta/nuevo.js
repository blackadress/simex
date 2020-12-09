window.onload = async () => {
  //await sleep(400)
  //CKEDITOR.instances["id_contenido"].resize('40vw', 400)
  //CKEDITOR.instances["id_alt_1-alternativa"].resize('40vw', 120)
  //CKEDITOR.instances["id_alt_2-alternativa"].resize('40vw', 120)
  //CKEDITOR.instances["id_alt_3-alternativa"].resize('40vw', 120)
  //CKEDITOR.instances["id_alt_4-alternativa"].resize('40vw', 120)
  //CKEDITOR.instances["id_alt_5-alternativa"].resize('40vw', 120)

  CKEDITOR.instances["id_contenido"].destroy()
  CKEDITOR.instances["id_alt_1-alternativa"].destroy()
  CKEDITOR.instances["id_alt_2-alternativa"].destroy()
  CKEDITOR.instances["id_alt_3-alternativa"].destroy()
  CKEDITOR.instances["id_alt_4-alternativa"].destroy()
  CKEDITOR.instances["id_alt_5-alternativa"].destroy()

  CKEDITOR.replace('id_contenido', {
    filebrowserUploadUrl: '/examen/api/upload-img/'
  })

};

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
