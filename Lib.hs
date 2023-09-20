replicate' :: Int -> a -> [a]
replicate' n x = [x | _ <- [1..n]]

factors :: Int -> [Int]
factors n = [x | x <- [1..n `div` 2], n `mod` x == 0]

perfects :: Int -> [Int]
perfects limit = [x | x <- [1..limit], sum (factors x) == x]

find :: (a -> Bool) -> [a] Maybe a

positions :: Eq a => a -> [a] -> [Int]
positions x xs = [i | (x', i) <- zip xs [0..], x == x']

scalarproduct :: Num a => [a] -> [a] -> a
scalarproduct xs ys = sum [ x * y | (x, y) <- zip xs ys]