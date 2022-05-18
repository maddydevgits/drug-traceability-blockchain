const drug = artifacts.require("drug");

module.exports = function (deployer) {
  deployer.deploy(drug);
};
