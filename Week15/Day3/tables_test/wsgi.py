from app_package import test_app

if __name__ == '__main__':
    from app_package import models
    test_app.run(debug=True, port=5500)
