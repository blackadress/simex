window.onload = () => {
  let button = document.querySelector("#filterButton");
  button.addEventListener("click", (e) => {
    e.preventDefault();
    const curso_id = document.querySelector("#curso").value;
    localStorage.setItem("curso_id", curso_id);
    // getting base direction
    const re = /.*buscar/
    const base_direction = re.exec(window.location.href)[0]

    // generating new direction
    const new_direction = `${base_direction}/${curso_id}/?page=1`;
    localStorage.setItem("new_direction", new_direction);
    location.replace(new_direction);
  });
};
