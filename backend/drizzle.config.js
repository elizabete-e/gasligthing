import { ENV } from "./src/config/env.js";

export default {
    schema: "./src/db/schema.js", // Path to the schema file
    out: "./src/db/migrations", // Output directory for migrations
    dialect: "postgresql", // Database dialect
    dbCredentials: { url: ENV.DATABASE_URL},
};