use itertools::Itertools;
use std::collections::{HashMap, VecDeque};
use std::fs;
use thousands::Separable;

fn shortest_path_length(
    graph: &HashMap<String, Vec<String>>,
    start: String,
    end: String,
) -> Option<usize> {
    let mut visited = HashMap::new();
    let mut queue = VecDeque::new();
    queue.push_back(start.clone());
    visited.insert(start, 0);
    while let Some(node) = queue.pop_front() {
        if node == end {
            return visited.get(&end).cloned();
        }
        for neighbour in graph.get(&node)? {
            if !visited.contains_key(neighbour) {
                visited.insert(neighbour.to_string(), visited[&node] + 1);
                queue.push_back(neighbour.to_string());
            }
        }
    }
    None
}

fn main() {
    let mut flow_rate: HashMap<String, i32> = HashMap::new();
    let mut graph: HashMap<String, Vec<String>> = HashMap::new();
    let mut valves: Vec<String> = Vec::new();
    let mut abridged_valves: Vec<String> = Vec::new();
    let mut distances: HashMap<(String, String), i32> = HashMap::new();

    let file = fs::read_to_string("data.txt").unwrap();
    for line in file.lines().collect::<Vec<&str>>() {
        let part = line.to_string().split_whitespace().collect::<Vec<&str>>()[1].to_string();
        let rate = line.to_string().split(";").collect::<Vec<&str>>()[0]
            .split("=")
            .collect::<Vec<&str>>()[1]
            .parse::<i32>()
            .unwrap();
        flow_rate.insert(part.clone(), rate);
        if line.contains(",") {
            graph.insert(
                part.clone(),
                line.split("valves ").collect::<Vec<&str>>()[1]
                    .split(", ")
                    .collect::<Vec<&str>>()
                    .iter()
                    .map(|s| s.to_string())
                    .collect(),
            );
        } else {
            graph.insert(
                part.clone(),
                vec![line.split_whitespace().collect::<Vec<&str>>()[9].to_string()],
            );
        }
        valves.push(part.clone());
        if rate > 0 {
            abridged_valves.push(part);
        }
    }

    for first in valves.clone() {
        for second in valves.clone() {
            if (first != second)
                && ((first == "AA") || (flow_rate.get(&first).unwrap() > &0))
                && ((second == "AA") || (flow_rate.get(&second).unwrap() > &0))
            {
                distances.insert(
                    (first.clone(), second.clone()),
                    shortest_path_length(&graph, first.clone(), second.clone())
                        .unwrap()
                        .try_into()
                        .unwrap(),
                );
            }
        }
    }

    let mut l = 0;
    let mut lens = Vec::new();
    for mut perm in abridged_valves
        .iter()
        .permutations(abridged_valves.len())
        .unique()
    {
        l += 1;
        println!("{:?}", l.separate_with_commas());
        let mut total = 0;
        let mut i = 0;
        let mut current = "AA";
        let mut processed = vec!["AA".to_string()];
        let mut processing = 0;
        while i < 30 {
            i += 1;
            for valve in &processed {
                total += flow_rate.get(valve).unwrap();
            }
            if processing > 0 {
                processing -= 1;
                continue;
            }
            if processed.contains(&current.to_string()) {
                if perm.len() == 0 {
                    continue;
                }
                let next = perm.pop().unwrap();
                let dist = distances.get(&(current.to_string(), next.clone())).unwrap();
                current = next;
                processing = dist - 1;
                continue;
            }
            processed.push(current.to_string());
        }
        lens.push(total);
    }

    println!("{:?}", lens.iter().max().unwrap());
}
