$(document).ready(function() {
    $('#predict-btn').click(function(event) {
        event.preventDefault();
        var data = {
            'Area': $('#area').val(),
            'Bedrooms': $('#bedrooms').val(),
            'Bathrooms': $('#bathrooms').val(),
            'Stories': $('#stories').val()
        };
        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: '/predict',
            data: JSON.stringify(data),
            success: function(response) {
                $('#result').text('Predicted price: $' + response.predicted_price);
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });
});
