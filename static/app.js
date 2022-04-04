"use strict";

const $cupcakeList = $("#cupcakeList");
const $submitForm = $("#submitCupcakeForm");
const $flavorInput = $("#flavor");
const $sizeInput = $("#size");
const $ratingInput = $("#rating");
const $imageInput = $("#image");

/** Handles page start */

async function start() {
  const cupcakes = await getCupcakesData();
  $cupcakeList.html("");
  showCupcakes(cupcakes);
}

/** Make GET request to API for all cupcakes. Returns list of cupcake instances */

async function getCupcakesData() {
  let response = await axios.get("/api/cupcakes");
  return response.data.cupcakes;
}

/** Populates DOM with cupcakes */

function showCupcakes(cupcakes) {
  for (let i = 0; i < cupcakes.length; i++) {
    let $html = createCupcakeHtml(cupcakes[i]);

    $cupcakeList.append($html);
  }
}

/** Takes cupcake object instance and returns html */

function createCupcakeHtml(cupcake) {
  let $html =
    $(`<li id=${cupcake.id}><img src="${cupcake.image}" alt="My ${cupcake.flavor} cupcake." /> Flavor:
${cupcake.flavor}, Size: ${cupcake.size}, Rating: ${cupcake.rating}</li>`);

  return $html;
}

/** Handles cupcake addition and adds new cupcake to list*/

async function handleForm(evt) {
  evt.preventDefault();

  const flavor = $flavorInput.val();
  const size = $sizeInput.val();
  const rating = $ratingInput.val();
  const image = $imageInput.val();

  const response = await axios.post("/api/cupcakes", {
    flavor,
    size,
    rating,
    image,
  });

  $flavorInput.val("");
  $sizeInput.val("");
  $ratingInput.val("");
  $imageInput.val("");

  $cupcakeList.append(createCupcakeHtml(response.data.cupcake));
}

start();
$submitForm.on("submit", handleForm);
