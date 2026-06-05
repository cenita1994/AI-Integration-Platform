// ====================================
// COMPUTER VISION
// CNN IMAGE CLASSIFICATION
// ====================================

let selectedImage = null;

// Get HTML elements

const dropArea = document.getElementById("dropArea");

const imageInput = document.getElementById("imageInput");

const previewImage = document.getElementById("previewImage");

const resultBox = document.getElementById("visionResult");

// ====================================
// CLICK TO UPLOAD
// ====================================

dropArea.addEventListener("click", function () {
  imageInput.click();
});

// ====================================
// SELECT IMAGE USING FILE BROWSER
// ====================================

imageInput.addEventListener("change", function () {
  selectedImage = this.files[0];

  displayPreview(selectedImage);
});

// ====================================
// DRAG IMAGE OVER AREA
// ====================================

dropArea.addEventListener("dragover", function (event) {
  event.preventDefault();

  dropArea.classList.add("border-primary");
});

// ====================================
// REMOVE DRAG EFFECT
// ====================================

dropArea.addEventListener("dragleave", function () {
  dropArea.classList.remove("border-primary");
});

// ====================================
// DROP IMAGE
// ====================================

dropArea.addEventListener("drop", function (event) {
  event.preventDefault();

  dropArea.classList.remove("border-primary");

  selectedImage = event.dataTransfer.files[0];

  displayPreview(selectedImage);
});

// ====================================
// DISPLAY IMAGE PREVIEW
// ====================================

function displayPreview(file) {
  if (!file) {
    return;
  }

  let reader = new FileReader();

  reader.onload = function (event) {
    previewImage.src = event.target.result;

    previewImage.style.display = "block";
  };

  reader.readAsDataURL(file);
}

// ====================================
// ANALYZE IMAGE
// ====================================

function analyzeImage() {
  if (selectedImage == null) {
    resultBox.innerHTML = `


      <div class="alert alert-danger">

        Please upload an image first.

      </div>


    `;

    return;
  }

  resultBox.innerHTML = `


    <div class="alert alert-warning">

      CNN model is analyzing image...

    </div>


  `;

  let formData = new FormData();

  formData.append(
    "image",

    selectedImage,
  );

  fetch("/analyze-image", {
    method: "POST",

    body: formData,
  })
    .then((response) => response.json())

    .then((result) => {
      resultBox.innerHTML = `



        <div class="alert alert-success">



          <h5 class="fw-bold">

            Prediction Result

          </h5>



          <h2 class="fw-bold text-primary">

            ${result.prediction}

          </h2>





          <hr>




          <h5 class="fw-bold">

            Confidence Score

          </h5>



          <p>

            ${result.confidence}

          </p>





          <hr>





          <h5 class="fw-bold">

            Interpretation

          </h5>




          <p>

            ${result.explanation}

          </p>




        </div>


      `;
    })

    .catch((error) => {
      resultBox.innerHTML = `


        <div class="alert alert-danger">

          Unable to process image classification.

        </div>


      `;
    });
}
