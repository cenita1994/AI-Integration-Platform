// ====================================
// COMPUTER VISION
// AI IMAGE VALIDATION + CNN CLASSIFICATION
// ====================================

let selectedImage = null;

// ====================================
// HTML ELEMENTS
// ====================================

const dropArea = document.getElementById("dropArea");

const imageInput = document.getElementById("imageInput");

const previewImage = document.getElementById("previewImage");

const resultBox = document.getElementById("visionResult");

// ====================================
// CLICK UPLOAD AREA
// ====================================

dropArea.addEventListener("click", function () {
  imageInput.click();
});

// ====================================
// FILE SELECT
// ====================================

imageInput.addEventListener("change", function () {
  selectedImage = this.files[0];

  displayPreview(selectedImage);
});

// ====================================
// DRAG OVER
// ====================================

dropArea.addEventListener("dragover", function (event) {
  event.preventDefault();

  dropArea.classList.add("border-primary");
});

// ====================================
// DRAG LEAVE
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
// IMAGE PREVIEW
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

  // Loading message

  resultBox.innerHTML = `


        <div class="alert alert-warning">


            AI is validating and analyzing image...


        </div>


    `;

  let formData = new FormData();

  formData.append(
    "image",

    selectedImage,
  );

  fetch(
    "/analyze-image",

    {
      method: "POST",

      body: formData,
    },
  )
    .then((response) => response.json())

    .then((result) => {
      // Similarity section

      let similaritySection = "";

      if (result.similarity) {
        similaritySection = `


                    <hr>


                    <h5 class="fw-bold">

                        Image Similarity Validation

                    </h5>


                    <p>

                        ${result.similarity}

                    </p>


                `;
      }

      // Display result

      resultBox.innerHTML = `


                <div class="alert alert-success">


                    <h5 class="fw-bold">

                        AI Prediction Result

                    </h5>



                    <h2 class="fw-bold text-primary">

                        ${result.prediction}

                    </h2>



                    ${similaritySection}



                    <hr>



                    <h5 class="fw-bold">

                        Confidence Score

                    </h5>



                    <p>

                        ${result.confidence}

                    </p>



                    <hr>



                    <h5 class="fw-bold">

                        AI Interpretation

                    </h5>



                    <p>

                        ${result.explanation}

                    </p>



                </div>


            `;
    })

    .catch((error) => {
      console.log(error);

      resultBox.innerHTML = `


                <div class="alert alert-danger">


                    Unable to process image classification.


                </div>


            `;
    });
}
