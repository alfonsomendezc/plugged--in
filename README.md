# Features:

1. **Conditional Navbar:** Displays different elements depending on whether the user is logged in or not..

2. **Fully Responsive Home Page:** Presents a general overview of the website in a modern and responsive manner. Descriptive cards, when clicked, navigate users to the relevant pages.

3. **Register & Login:** Includes toggle hide password, password confirmation, and regex for email and password inputs.

4. **Profile Page:** Features user description, favorite game, region, platform, contact form, and profile picture. Also, it shows a list of posts made by the user. Posts can be deleted if the user chooses to do so on /your-profile. Utilizes the Cloudinary API for image upload, MUI Text inputs, and an MUI Autocomplete component that fetches data from the RAWG API to display a list of video games for the user to choose from. The Region and Platform Select component include custom images..

5. **Find Gamers:** The principal functionality of the website. Users can publish posts specifying a Title, Video-game (Fetched from the RAWG API), and Description. The date is automatically added. The rest of the post's data is fetched from the backend along with the profile information. Users can contact each other with the contact form provided. User profiles can be viewed by clicking on the username or profile picture on the post. There's also a possibility to comment on the post. Nested filter buttons enable users to filter posts by region, platform, and game simultaneously.

6. **Game Wiki:** A responsive video game database (Information fetched from the RAWG API). It displays cards with the game's image, platform count, and release date. Users can search in real-time, yielding a substantial number of results. The detail button directs the user to a specific game page.

7. **Game Detail:**  Provides general information about a video game, including Metascore Rating, image, list of platforms, general description, release date, official website, Reddit, Twitch count, YouTube count, and tags (Information fetched from the RAWG API).

--- 
## Frontend Stack:

1. **React:** A JavaScript library for building user interfaces.
2. **React Router:** A library for handling routing in React applications.
3. **Styled Components:** A library for styling React components using tagged template literals.
4. **Emotion:** A library for writing CSS styles with JavaScript.
5. **Material-UI (MUI):** A React UI framework implementing Google's Material Design.
6. **Prop-types:** A library for type-checking React props.

## Build Tools and Bundlers:

1. **Webpack:** A module bundler for JavaScript applications.
2. **Babel:** A JavaScript compiler that allows you to use the latest ECMAScript features.
3. **ESLint:** A tool for identifying and reporting patterns found in ECMAScript/JavaScript code.

## Backend Stack (for tooling and development):

- **Node.js:** A JavaScript runtime for server-side development.
- **JWT Decode:** A library for decoding JSON Web Tokens.

## Backend Stack:

1. **Flask:** A micro web framework for Python.
2. **Flask-Migrate:** Extension for Flask to handle database migrations with SQLAlchemy.
3. **Flask-Swagger:** Extension for generating Swagger documentation for Flask APIs.
4. **Flask-CORS:** Extension for handling Cross-Origin Resource Sharing (CORS) in Flask applications.
5. **Flask-JWT-Extended:** Extension for handling JSON Web Tokens (JWT) in Flask applications.

- **JWT (JSON Web Token):** Used for authentication and token-based security.
  
## Database and ORM:

- **SQLAlchemy:** A SQL toolkit and Object-Relational Mapping (ORM) library for Python.

## Other Utilities:

- **React Fade In:** A library for adding fade-in effects to React components.
- **React Toastify:** A library for displaying toasts (pop-up notifications) in React applications.
- **React Tooltip:** A library for adding tooltips to React components.

---

© Plugged In. This website is for practice and educational purposes. All content displayed is used under fair use or with proper attribution to respective owners. If you believe content infringes your rights, please contact me.
