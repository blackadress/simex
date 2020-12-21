window.onload = () => {
  let valores_alternativas = document.querySelector("#valores-alternativas")
    .children;
  valores_alternativas = parse(Array.from(valores_alternativas));
  llenar(valores_alternativas);
};

const parse = (divs) => {
  const valores = divs.map((div) => {
    const alternativa = div.children[0].value;
    const correcta = div.children[1].value;
    return { alternativa, correcta };
  });

  return valores;
};

const llenar = (valores) => {
  const insertIntoCkeditor = (str, editor) => {
    CKEDITOR.instances[editor].setData(str);
  };

  let contador = 2;

  valores.map((valor) => {
    console.log(valor.correcta)
    if (valor.correcta === 'True') {
      insertIntoCkeditor(valor.alternativa, "id_alt_1-alternativa");
    } else {
      const editor = `id_alt_${contador}-alternativa`
      console.log(editor)
      insertIntoCkeditor(valor.alternativa, editor);
      contador += 1;
    }
  });
};
