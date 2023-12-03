use std::fs;

fn main() {
    let file_content = fs::read_to_string("input.txt").expect("Couldn't open file");
    let lines = file_content.trim().lines();

    let mut part_one = 0;
    for line in lines.clone() {

        let mut numbers: Vec<i32> = Vec::new();
        for char in line.chars(){
            if char.is_numeric(){
                numbers.push(char.to_string().parse::<i32>().unwrap());
            }
        }
        if !numbers.is_empty(){
            let first = numbers.first().unwrap();
            let last = numbers.last().unwrap_or(first);
            part_one += first * 10 + last;
        }
    } 
    println!("{}", part_one);
}
        