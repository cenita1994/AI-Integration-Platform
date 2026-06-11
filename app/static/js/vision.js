// ====================================
// COMPUTER VISION
// CNN IMAGE CLASSIFICATION
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

if (dropArea && imageInput) {
  dropArea.addEventListener("click", function () {
    imageInput.click();
  });
}

// ====================================
// FILE SELECT
// ====================================

if (imageInput) {
  imageInput.addEventListener("change", function () {
    selectedImage = this.files[0];

    displayPreview(selectedImage);
  });
}

// ====================================
// DRAG OVER
// ====================================

if (dropArea) {
  dropArea.addEventListener("dragover", function (event) {
    event.preventDefault();

    dropArea.classList.add("border-primary");
  });
}

// ====================================
// DRAG LEAVE
// ====================================

if (dropArea) {
  dropArea.addEventListener("dragleave", function () {
    dropArea.classList.remove("border-primary");
  });
}

// ====================================
// DROP IMAGE
// ====================================

if (dropArea) {
  dropArea.addEventListener("drop", function (event) {
    event.preventDefault();

    dropArea.classList.remove("border-primary");

    selectedImage = event.dataTransfer.files[0];

    displayPreview(selectedImage);
  });
}

// ====================================
// IMAGE PREVIEW
// ====================================

function displayPreview(file) {
  if (!file) {
    return;
  }

  if (!file.type.startsWith("image/")) {
    resultBox.innerHTML = `
      <div class="alert alert-danger">
        Please upload a valid image file.
      </div>
    `;

    selectedImage = null;

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

async function analyzeImage() {
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
      AI is analyzing image. Please wait...
    </div>
  `;

  let formData = new FormData();

  formData.append("image", selectedImage);

  try {
    console.log("Sending image to backend...");

    const response = await fetch("/analyze-image", {
      method: "POST",
      body: formData,
    });

    const text = await response.text();

    console.log("Raw server response:", text);

    if (!text) {
      throw new Error(
        "Server returned an empty response. The backend may have stopped during image processing.",
      );
    }

    let result;

    try {
      result = JSON.parse(text);
    } catch (error) {
      throw new Error("Server returned a non-JSON response: " + text);
    }

    if (!response.ok) {
      throw new Error(result.error || "Server error occurred.");
    }

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
  } catch (error) {
    console.log("Vision Error:", error);

    resultBox.innerHTML = `
      <div class="alert alert-danger">

        <h5 class="fw-bold">
          Unable to process image classification.
        </h5>

        <small>
          ${error.message}
        </small>

      </div>
    `;
  }
}

// Make function available to HTML onclick
window.analyzeImage = analyzeImage;
