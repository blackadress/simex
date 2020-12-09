window.onload = () => {
  let button = document.querySelector("#filterButton");
  button.addEventListener("click", (e) => {
    e.preventDefault();
    const universidad_id = document.querySelector("#universidad").value;
    localStorage.setItem("universidad_id", universidad_id);
    // getting base direction
    const re = /.*buscar/
    const base_direction = re.exec(window.location.href)[0]

    // generating new direction
    const new_direction = `${base_direction}/${universidad_id}/?page=1`;
    localStorage.setItem("new_direction", new_direction);
    location.replace(new_direction);
  });
};
