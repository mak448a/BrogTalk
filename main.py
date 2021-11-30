from website import create_app


app = create_app()
# app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == "__main__":
  from waitress import serve
  print("Started app")
  serve(app, host="0.0.0.0", port=8080)
