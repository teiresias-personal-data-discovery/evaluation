const mocker = require("mocker-data-generator").default;
const fs = require("fs");

const user = {
  firstName: {
    faker: "name.firstName",
  },
  lastName: {
    faker: "name.lastName",
  },
  ipv4: { faker: "internet.ip" },
};

mocker()
  .schema("user", user, 5000)
  .build()
  .then((data) => JSON.stringify(data.user))
  .then((json) => {
    fs.writeFile("../../mock_users.json", json, (err) => {
      if (err) {
        throw err;
      }
      console.log("JSON file has been saved.");
    });
  })
  .catch((err) => console.error(err));
