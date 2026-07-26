# Nova Shop

Nova Shop is a fully functional e-commerce frontend written in **AAYU**, a declarative UI language.

## Architecture
The project follows a modern component-based architecture:
- `src/main.aayu` : Application entry point
- `src/app/` : Contains global state and actions (business logic)
- `src/pages/` : Contains individual screens (Home, Cart, Login, Signup, Account)
- `src/components/` : Contains reusable UI components (e.g. Navigation Bars)

## Running the Project
This project must be compiled and executed using the **AAYU Compiler**. 

Assuming you have the AAYU Compiler locally:
1. Copy this `src` directory into the AAYU compiler's root folder.
2. Start the AAYU backend VM:
   ```bash
   python serve_app.py src/main.aayu
   ```
3. Open your browser and navigate to `http://localhost:3000`.

## Features
- **Session Isolation:** Powered by the AAYU Virtual Machine, multiple browser tabs do not interfere with each other's state (Cart, Login Status).
- **Fast Action Pipeline:** UI interactions (like clicking buttons or typing in inputs) respond locally at ~60fps via SSE streams.
- **Secure State:** Built-in isolation per user connection.

Enjoy building with AAYU!