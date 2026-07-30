# Nova Shop

Nova Shop is a fully functional e-commerce frontend written in **AAYU**, a declarative UI language.

## Architecture
The project follows a modern component-based architecture:
- src/main.aayu : Application entry point
- src/app/ : Contains global state and actions (business logic)
- src/pages/ : Contains individual screens (Home, Cart, Login, Signup, Account)
- src/components/ : Contains reusable UI components (e.g. Navigation Bars)

## Running the Project

This project uses the modern AAYU Package Manager.

1. Install the AAYU Compiler:
   ``bash
   pip install aayu-lang
   ``
2. Run the project in development mode:
   ``bash
   aayu run
   ``
3. Build for production:
   ``bash
   aayu build
   ``

## Features
- **Session Isolation:** Powered by the AAYU Virtual Machine, multiple browser tabs do not interfere with each other's state (Cart, Login Status).
- **Fast Action Pipeline:** UI interactions respond locally at ~60fps via SSE streams.
- **Secure State:** Built-in isolation per user connection.

Enjoy building with AAYU!
