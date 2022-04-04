"use strict";

const $cupcakeList = $("#cupcakeList");
const $submitForm = $("#submitCupcakeForm");
const $flavorInput = $("#flavor");
const $sizeInput = $("#size");
const $ratingInput = $("#rating");
const $imageInput = $("#image");

/** Clear and populate cupcakes list */

async function showCupcakes() {
  $cupcakeList.html("");
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

/** Handles cupcake addition and adds new cupcake to list*/

async function handleForm(evt) {
  evt.preventDefault();

  const flavor = $flavorInput.val();
  const size = $sizeInput.val();
  const rating = $ratingInput.val();
  const image = $imageInput.val();

  await axios.post("/api/cupcakes", {
    flavor,
    size,
    rating,
    image,
  });

  $flavorInput.val("");
  $sizeInput.val("");
  $ratingInput.val("");
  $imageInput.val("");
  showCupcakes();
}

showCupcakes();
$submitForm.on("submit", handleForm);
