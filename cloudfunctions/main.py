from flask import jsonify

def my_http_function(request, context):
    # Extract the request data
    name = request.args.get('name')

    # Construct the response
    message = f"Hello, {name}!"
    response = {'message': message}

    # Return the response as JSON
    return jsonify(response)

    