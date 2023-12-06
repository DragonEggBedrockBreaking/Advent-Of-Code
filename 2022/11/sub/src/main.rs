use std::collections::HashMap;
use std::fs;

fn main() {
    let content = fs::read_to_string("data.txt").unwrap();
    let mut lines = content.lines();

    let num = 8;

    let mut monkeys = Vec::new();
    let mut inspections = Vec::new();
    for _ in 0..num {
        let temp: Vec<u128> = Vec::new();
        monkeys.push(temp);
        inspections.push(0);
    }

    let mut monkey_data = HashMap::new();

    for i in 0..num {
        lines.next();
        for item in lines
            .next()
            .unwrap()
            .split(": ")
            .last()
            .unwrap()
            .split(", ")
        {
            monkeys[i].push(item.parse::<u128>().unwrap());
        }
        monkey_data.insert(
            i.to_string() + "_operation",
            lines.next().unwrap().split("= ").last().unwrap(),
        );
        monkey_data.insert(
            i.to_string() + "_test",
            lines.next().unwrap().split("by ").last().unwrap(),
        );
        monkey_data.insert(
            i.to_string() + "_true",
            lines.next().unwrap().split("monkey ").last().unwrap(),
        );
        monkey_data.insert(
            i.to_string() + "_false",
            lines.next().unwrap().split("monkey ").last().unwrap(),
        );
        lines.next();
    }

    for j in 0..20 {
        println!("{}", j);
        for i in 0..monkeys.len() {
            while monkeys[i].len() > 0 {
                inspections[i] += 1;

                let mut item: u128 = monkeys[i][0];

                let operation = monkey_data[&(i.to_string() + "_operation")];
                if operation == "old * old" {
                    item = item.pow(2);
                } else if operation.contains("*") {
                    item *= operation
                        .split_whitespace()
                        .last()
                        .unwrap()
                        .parse::<u128>()
                        .unwrap();
                } else if operation.contains("+") {
                    item += operation
                        .split_whitespace()
                        .last()
                        .unwrap()
                        .parse::<u128>()
                        .unwrap();
                } else {
                    println!("{}", operation);
                }

                if item
                    % monkey_data[&(i.to_string() + "_test")]
                        .parse::<u128>()
                        .unwrap()
                    == 0
                {
                    monkeys[monkey_data[&(i.to_string() + "_true")]
                        .parse::<usize>()
                        .unwrap()]
                    .push(item);
                } else {
                    monkeys[monkey_data[&(i.to_string() + "_false")]
                        .parse::<usize>()
                        .unwrap()]
                    .push(item);
                }

                monkeys[i].remove(0);
            }
        }
    }

    let max = *inspections.iter().max().unwrap();
    inspections.remove(inspections.iter().position(|x| *x == max).unwrap());
    println!("{}", max * *inspections.iter().max().unwrap());
}
