// ====================================
// BUY COMPUTER PREDICTION
// RANDOM FOREST + FLASK API
// ====================================

function predict() {
  // Result container

  let resultText = document.getElementById("result");

  // Loading message

  resultText.innerHTML = `

        <div class="alert alert-warning">

            Analyzing customer information...

        </div>

    `;

  // Get user input

  let data = {
    age: document.getElementById("age").value,

    income: document.getElementById("income").value,

    student: document.getElementById("student").value,

    credit_rating: document.getElementById("credit").value,
  };

  // Send data to Flask API

  fetch("/predict", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify(data),
  })
    // Convert response

    .then((response) => response.json())

    // Display prediction result

    .then((result) => {
      resultText.innerHTML = `


            <div class="alert alert-success">


                <h5 class="fw-bold">

                    Prediction Result

                </h5>



                <h2 class="fw-bold">

                    ${result.prediction}

                </h2>



                <hr>



                <h5 class="fw-bold">

                    Gemini AI Explanation

                </h5>



                <p>

                    ${result.explanation}

                </p>



            </div>


        `;
    })

    // Error handling

    .catch((error) => {
      resultText.innerHTML = `


            <div class="alert alert-danger">


                Unable to connect to prediction server.


            </div>


        `;
    });
}
