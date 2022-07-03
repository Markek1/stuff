use rand::prelude::SliceRandom;

fn main() {
    let mut successes = 0;
    let total = 10_000;

    for _ in 0..total {
        let mut nums: Vec<usize> = (0..100).collect();
        nums.shuffle(&mut rand::thread_rng());

        if (|| {
            for prisoner_number in 0..nums.len() {
                let mut boxes_checked = 0;
                let mut next_to_check = prisoner_number;
                loop {
                    next_to_check = nums[next_to_check];
                    if next_to_check == prisoner_number {
                        break;
                    }

                    boxes_checked += 1;
                    if boxes_checked >= 50 {
                        return false;
                    }
                }
            }
            true
        })() {
            successes += 1;
        }
    }

    println!("{}%", successes as f64 / total as f64);
}
