import { drizzle } from 'drizzle-orm/neon-http';
import { neon } from "@neondatabase/serverless";
import {ENV } from "./env.js";
import * as schema from "../db/schema.js";

const sql = neon(ENV.DATABASE_URL); // Initialize the Neon client with the database URL from environment variables
export const db = drizzle(sql, { schema }); // Create a Drizzle ORM instance with the Neon client and the schema
