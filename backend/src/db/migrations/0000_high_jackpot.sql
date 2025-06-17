CREATE TABLE "last_matches" (
	"id" serial PRIMARY KEY NOT NULL,
	"userid" integer NOT NULL,
	"placement" integer NOT NULL,
	"user_score" integer NOT NULL,
	"created_at" timestamp DEFAULT now()
);
