import { pgTable, serial, text, timestamp, integer } from "drizzle-orm/pg-core";

export const lastMatches = pgTable("last_matches", {
    id: serial("id").primaryKey(),
    userid: integer("userid").notNull(),
    matchid: text("matchid").notNull(),
    placement: integer("placement").notNull(),
    userScore: integer("user_score").notNull(),
    createdAt: timestamp("created_at").defaultNow(),
});