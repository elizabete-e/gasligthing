import cron from 'cron';
import https from 'https';

const job = new cron.CronJob('*/14 * * * *', function () {
    https
        .get(process.env.API_URL, (res) => {
            if (res.statusCode === 200) console.log('Cron job executed successfully');
            else console.log('Cron job failed with status code:', res.statusCode);
        })
        .on("error", (e) => console.error("Error in cron job:", e));

});

export default job;

//cron job to run every 14 minutes
//it sends a GET request to the API_URL
//to keep the server alive and prevent it from going to sleep