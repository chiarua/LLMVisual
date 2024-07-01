import { QueryConfig } from './config';
import { WildcardIndex } from './wildcardindex';
import { SpecQueryModel } from './model';
import { Property } from './property';
import { Schema } from './schema';
export interface Enumerator {
    (answerSets: SpecQueryModel[], specM: SpecQueryModel): SpecQueryModel[];
}
export declare function getEnumerator(prop: Property): EnumeratorFactory;
export interface EnumeratorFactory {
    (wildcardIndex: WildcardIndex, schema: Schema, opt: QueryConfig): Enumerator;
}
/**
 * @param prop property type.
 * @return an answer set reducer factory for the given prop.
 */
export declare function EncodingPropertyGeneratorFactory(prop: Property): EnumeratorFactory;
