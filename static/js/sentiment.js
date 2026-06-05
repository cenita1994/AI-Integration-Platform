// ====================================
// SENTIMENT ANALYSIS
// NLP + MACHINE LEARNING + AI
// ====================================

function analyzeSentiment() {
  let resultBox = document.getElementById("sentimentResult");

  let tweet = document.getElementById("tweet").value;

  // Validate input

  if (tweet.trim() === "") {
    resultBox.innerHTML = `

      <div class="alert alert-danger">

        Please enter a text before analyzing.

      </div>

    `;

    return;
  }

  // Loading message

  resultBox.innerHTML = `

    <div class="alert alert-warning">

      Analyzing sentiment...

    </div>

  `;

  // Send request to Flask API

  fetch("/analyze-sentiment", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      tweet: tweet,
    }),
  })
    .then((response) => response.json())

    .then((result) => {
      resultBox.innerHTML = `


      <div class="alert alert-success">


        <h5 class="fw-bold">

          Sentiment Prediction

        </h5>


        <h2 class="fw-bold">

          ${result.sentiment}

        </h2>



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

        Unable to connect to sentiment analysis server.

      </div>


    `;
    });
}
