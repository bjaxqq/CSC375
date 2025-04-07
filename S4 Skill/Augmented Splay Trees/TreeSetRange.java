/*******************
 * TreeSetRange
 * Author: Christian Duncan
 * 
 * This version uses Java's built-in TreeSet (Red-Black Tree)
 * but it does not efficiently handle sizes. So any range count
 * will ultimately be linear instead of logarithmic.
 * Useful for testing purposes.
 *******************/
import java.util.TreeSet;
import java.util.Set;

public class TreeSetRange<E> {
    TreeSet<E> internalTree;

    public TreeSetRange() {
        internalTree = new TreeSet<>();
    }

    public void insert(E element) {
        internalTree.add(element);
    }

    public boolean delete(E element) {
        return internalTree.remove(element);
    }

    // Returns how many elements are between a (inclusive) and b (inclusive)
    public int rangeCount(E a, E b) {
        // Get how many elements are less than b
        // Set<E> rangeSet = internalTree.subSet(a, true, b, true);
        // return rangeSet.size();
        Set<E> aSet = internalTree.headSet(a, false);  // Don't count a
        Set<E> bSet = internalTree.headSet(b, true);   // Count b
        return bSet.size() - aSet.size();
    }
}