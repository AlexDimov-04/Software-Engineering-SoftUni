function sprintReview(array) {
    let n = Number(array.shift());
    let sprintBoard = {};
    let commandParser = {
        'Add New': addNewTask,
        'Change Status': changeStatus,
        'Remove Task': removeTask
    };
    let toDoPoints = 0;
    let inProgressPoints = 0;
    let codeReviewPoints = 0;
    let donePoints = 0;

    for (let index = 1; index <= n; index++) {
        let [assignee, taskId, title, status, estimatedPoints] = array.shift().split(':');

        if (sprintBoard.hasOwnProperty(assignee)) {
            sprintBoard[assignee].push({ taskId, title, status, estimatedPoints });
        } else {
            sprintBoard[assignee] = [{ taskId, title, status, estimatedPoints }];
        }
    }

    for (const line of array) {
        let command = line.split(':');
        commandParser[command[0]](...command.slice(1));
    }

    printResultPoints();

    function addNewTask(assignee, taskId, title, status, estimatedPoints) {
        if (!sprintBoard.hasOwnProperty(assignee)) {
            console.log(`Assignee ${assignee} does not exist on the board!`)
        } else {
            sprintBoard[assignee].push({ taskId, title, status, estimatedPoints });
        }
    }

    function changeStatus(assignee, taskId, newStatus) {
        if (!sprintBoard.hasOwnProperty(assignee)) {
            console.log(`Assignee ${assignee} does not exist on the board!`)
            return;
        }
        for (const line of sprintBoard[assignee]) {
            if (line['taskId'] !== taskId) {
                console.log(`Task with ID ${taskId} does not exist for ${assignee}!`);
                return;
            }
        }

        for (const line of sprintBoard[assignee]) {
            if (line['taskId'] === taskId) {
                line['status'] = newStatus;
            }
        }
    }

    function removeTask(assignee, index) {
        if (!sprintBoard.hasOwnProperty(assignee)) {
            console.log(`Assignee ${assignee} does not exist on the board!`)
        }
        else if (Number(index) >= sprintBoard[assignee].length || Number(index) < 0) {
            console.log('Index is out of range!');
        } else {
            sprintBoard[assignee].splice(index, 1);
        }

    }

    function printResultPoints() {
        for (const [_key, tasks] of Object.entries(sprintBoard)) {
            for (const line of tasks) {
                if (line === undefined) {
                    continue;
                }
                if (line['status'] === 'ToDo') {
                    toDoPoints += Number(line['estimatedPoints']);
                }
                else if (line['status'] === 'In Progress') {
                    inProgressPoints += Number(line['estimatedPoints']);
                }
                else if (line['status'] === 'Code Review') {
                    codeReviewPoints += Number(line['estimatedPoints']);
                }
                else if (line['status'] === 'Done') {
                    donePoints += Number(line['estimatedPoints']);
                }
            }
        }

        console.log(`ToDo: ${toDoPoints}pts`)
        console.log(`In Progress: ${inProgressPoints}pts`)
        console.log(`Code Review: ${codeReviewPoints}pts`)
        console.log(`Done Points: ${donePoints}pts`)

        if (donePoints >= (toDoPoints + inProgressPoints + codeReviewPoints)) {
            console.log('Sprint was successful!');
        } else {
            console.log('Sprint was unsuccessful...');
        }
    }
}

sprintReview([
    '5',
    'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
    'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
    'Peter:BOP-1211:POC:Code Review:5',
    'Georgi:BOP-1212:Investigation Task:Done:2',
    'Mariya:BOP-1213:New Account Page:In Progress:13',
    'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
    'Change Status:Peter:BOP-1290:ToDo',
    'Remove Task:Mariya:1',
    'Remove Task:Joro:1',
])