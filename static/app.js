"use strict";

const $cupcakeList = $("#cupcakeList");

async function showCupcakes() {
  let response = await axios.get("/api/cupcakes");

  const cupcakes = response.data.cupcakes;
  for (let i = 0; i < cupcakes.length; i++) {
    let id = cupcakes[i].id;
    let flavor = cupcakes[i].flavor;
    let image = cupcakes[i].image;
    let rating = cupcakes[i].rating;
    let size = cupcakes[i].size;

    let $html =
      $(`<li id=${id}><img src="${image}" alt="My ${flavor} cupcake." /> Flavor:
    ${flavor}, Size: ${size}, Rating: ${rating}</li>`);

    $cupcakeList.append($html);
  }
}

showCupcakes();
