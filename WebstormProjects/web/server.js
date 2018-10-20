const express = require('express'),
    app = express();
app.use(express.static('sait'));
app.listen(3000, () => console.log("Server is started on port 3000"));