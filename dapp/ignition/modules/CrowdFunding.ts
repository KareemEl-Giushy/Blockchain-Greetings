import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

export default buildModule('app', (m) => {
    const app = m.contract("CrowdFunding");

    console.log(m.call(app, "working"));

    return {app};
});