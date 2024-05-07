import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

export default buildModule("HelloWorldApp", (m) => {
    const helloWorld = m.contract("HelloWorld");

    return { helloWorld };
});