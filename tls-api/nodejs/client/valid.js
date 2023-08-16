const axios = require('axios');
const agent = require('./agent');
const port = 4433;

const serverUrl = 'https://localhost:4433/authenticate';
let opts = { httpsAgent: agent('alice') };

axios.get(serverUrl, opts)
	.then((res) => {
		console.log(res.data);
	})
	.catch((err) => {
		console.error(err.response.data);
	});