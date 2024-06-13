$(document).ready(function() {
    $('#predict-btn').click(function(event) {
        event.preventDefault();
        var formData = {
            'Area': $('#area').val(),
            'Bedrooms': $('#bedrooms').val(),
            'Bathrooms': $('#bathrooms').val(),
            'Stories': $('#stories').val()
        };

        $.ajax({
            type: 'POST',
            url: '/predict',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                if (response.predicted_price !== undefined) { // Check if predicted_price is defined
                    $('#result').text('Predicted Price: $' + response.predicted_price);
                } else {
                    $('#result').text('Prediction Error: ' + response.error);
                }
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });
});
