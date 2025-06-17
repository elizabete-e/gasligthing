import express from "express";
import { db }  from "./config/db.js"; // Database connection
import { ENV } from "./config/env.js"; //to load environment variables
import { lastMatches } from "./db/schema.js";
import { and, eq } from "drizzle-orm";

const app = express();
const PORT = ENV.PORT || 5001; // Default port

app.use(express.json()); // Middleware to parse JSON bodies

app.get("/api/health", (req, res) => {
    res.status(200).json({ success: "Server is healthy" });
});

app.get("/api/last_matches/:userid", async (req, res) => {
    
    try {
        const { userid } = req.params;
        const userMatches = await db.select().from(lastMatches).where(eq(lastMatches.userid, userid));
        res.status(200).json(userMatches);
    } catch (error) {
        console.error("Error fetching last matches:", error);
        res.status(500).json({ error: "Error fetching last matches" });
    }
});

app.post('/api/last_match', async (req, res) => {
    try {
        const { userid, matchid, placement, user_score } = req.body;
        if (!userid || !matchid || !placement || !user_score) {
            return res.status(400).json({ error: 'Missing required fields' });
        }
        const newLastMatch = await db.insert(lastMatches).values({
            userid,
            matchid,
            placement,
            userScore: user_score,
        }).returning();
        res.json(newLastMatch[0]); // Return the newly added match

    } catch (error) {
        console.error('Error adding last match:', error);
        res.status(500).json({ error: 'Error adding last match' });
    }
});

app.delete("/api/delete_match/:userid/:matchid", async (req, res) => {
    
    try {
        const { userid, matchid } = req.params
        await db.delete(lastMatches).where(
            and(eq(lastMatches.userid, userid), eq(lastMatches.matchid, matchid))
        ).returning();
        res.status(200).json({ message: "Match deleted successfully" });

    } catch (error) {
        console.error("Error deleting last match:", error);
        res.status(500).json({ error: "Error deleting last match" });
    }
});

app.listen(PORT, () => {
    console.log("Server is on " + PORT);
});